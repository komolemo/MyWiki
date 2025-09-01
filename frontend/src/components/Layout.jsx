// Layout.jsx
import React, { useState } from 'react';
import Header from '../components/Header/Header.jsx';
import Sidebar from '../components/Sidebar/Sidebar.jsx';
import { Outlet } from 'react-router-dom';

const Layout = () => {
    const [sidebarVisible, setSidebarVisible] = useState(true);

    const toggleSidebar = () => {
    setSidebarVisible(prev => !prev);
    };
    return (
        <main className="h-screen flex flex-col w-full">
            <Header toggleSidebar={toggleSidebar} />
            <div className="flex flex-1">
                <Sidebar visible={sidebarVisible} />
                <Outlet /> {/* 各ページのコンテンツがここに差し込まれる */}
            </div>
        </main>
    )
};

export default Layout;