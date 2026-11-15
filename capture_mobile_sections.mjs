import { spawn } from 'child_process';
import fs from 'fs';

async function run() {
  const PORT = 9891;
  const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
    '--headless=new',
    `--remote-debugging-port=${PORT}`,
    '--user-data-dir=/tmp/chrome_prof_9891',
    '--disable-gpu',
    '--hide-scrollbars',
    'about:blank'
  ]);

  let targets = null;
  for (let i = 0; i < 30; i++) {
    try {
      let res = await fetch(`http://127.0.0.1:${PORT}/json/list`);
      targets = await res.json();
      if (targets && targets.length > 0) break;
    } catch (e) {}
    await new Promise(r => setTimeout(r, 200));
  }

  if (!targets || targets.length === 0) {
    chrome.kill();
    throw new Error('Chrome did not initialize on port ' + PORT);
  }

  const ws = new WebSocket(targets[0].webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);

  let msgId = 1;
  const callbacks = new Map();
  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.id && callbacks.has(data.id)) {
      callbacks.get(data.id)(data);
      callbacks.delete(data.id);
    }
  };

  function send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = msgId++;
      callbacks.set(id, (res) => {
        if (res.error) reject(res.error);
        else resolve(res.result);
      });
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  await send('Page.enable');
  await send('Emulation.setDeviceMetricsOverride', {
    width: 393,
    height: 852,
    deviceScaleFactor: 2,
    mobile: true
  });

  console.log('Navigating to Version 3 (All events)...');
  await send('Page.navigate', { url: 'http://localhost:8080/version-3/index.html?opened=1' });
  await new Promise(r => setTimeout(r, 2200));

  fs.mkdirSync('screenshots', { recursive: true });

  const sections = [
    'heroSection',
    'sangeetHaldiSection',
    'shaadiReceptionSection',
    'footerSection'
  ];

  for (const sec of sections) {
    console.log(`Capturing section: ${sec}...`);
    const rectRes = await send('Runtime.evaluate', {
      expression: `
        (() => {
          const el = document.getElementById('${sec}');
          if (!el) return null;
          const r = el.getBoundingClientRect();
          return {
            x: 0,
            y: Math.max(0, Math.round(r.top + window.scrollY)),
            width: 393,
            height: Math.min(852, Math.round(r.height)),
            scale: 1
          };
        })()
      `,
      returnByValue: true
    });

    const clip = rectRes.result.value;
    console.log(`Clip for ${sec}:`, clip);

    const shot = await send('Page.captureScreenshot', {
      format: 'png',
      clip: clip || { x: 0, y: 0, width: 393, height: 852, scale: 1 },
      captureBeyondViewport: true
    });
    const buffer = Buffer.from(shot.data, 'base64');
    fs.writeFileSync(`screenshots/new_${sec}.png`, buffer);
    console.log(`Saved screenshots/new_${sec}.png`);
  }

  ws.close();
  chrome.kill();
  console.log('All new painting screens captured successfully!');
  process.exit(0);
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});
