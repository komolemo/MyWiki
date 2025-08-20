const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('api', {
  readCategories: (dirPath) => ipcRenderer.invoke('read-categories', dirPath),
  readArticles: (dirPath) => ipcRenderer.invoke('read-articles', dirPath),
  readArticle: (filePath) => ipcRenderer.invoke('read-article', filePath),
});
