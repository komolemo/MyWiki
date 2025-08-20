import { app, BrowserWindow, ipcMain } from 'electron';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

// __dirname の代替
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

ipcMain.handle('read-categories', async (dirPath) => {
  return fs.readdirSync(path.resolve(dirPath));
});

ipcMain.handle('read-articles', async (dirPath) => {
  return fs.readdirSync(path.resolve(dirPath));
});

ipcMain.handle('read-article', async (filePath) => {
  return fs.readFileSync(path.resolve(filePath), 'utf-8');
});

function createWindow() {
  const win = new BrowserWindow({
    width: 1000,
    height: 700,
    webPreferences: {
      contextIsolation: true,
      preload: join(__dirname, 'preload.js'),
    },
  });

  win.loadURL('http://localhost:5173');
}

app.whenReady().then(createWindow);
