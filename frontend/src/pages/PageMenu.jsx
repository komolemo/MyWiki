import React, { useState } from 'react';
import Header from '../components/Header';
import Sidebar from '../components/Sidebar';
import Article from '../components/Article';

const App = () => {
  const [sidebarVisible, setSidebarVisible] = useState(true);

  const toggleSidebar = () => {
    setSidebarVisible(prev => !prev);
  };

  return (
    <div className="h-screen flex flex-col w-full">
      <Header toggleSidebar={toggleSidebar} />
      <div className="flex flex-1">
        <Sidebar visible={sidebarVisible} />
        <Article />
      </div>
    </div>
  );
}

export default App;