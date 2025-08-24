// Layout.jsx
import Header from './Header';
import { Outlet } from 'react-router-dom';

const Layout = () => (
    <>
        {/* <Header /> */}
        <main>
            <div className='flex'>
                <Outlet /> {/* 各ページのコンテンツがここに差し込まれる */}
            </div>
        </main>
    </>
);

export default Layout;