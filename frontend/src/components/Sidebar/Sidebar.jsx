import React from 'react';
import ThemeToggle from './ToggleButton';

export default function Sidebar({ visible }) {
  const toggleTheme = () => {
    const html = document.documentElement;
    if (html.classList.contains('dark')) {
      html.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    } else {
      html.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    }
  };

  return (
    <nav className={`${visible ? 'block' : 'hidden'} w-56 bg-gray-100 dark:bg-gray-800 text-black dark:text-white border-r p-4 flex flex-col justify-between`}>
      <div>
        <h3 className="text-lg font-semibold mb-2">カテゴリー</h3>
        <ul className="space-y-2">
          <li>📁 技術</li>
          <li>📁 メモ</li>
          <li>📁 リンク集</li>
        </ul>
      </div>
      <div className="flex mt-4 items-center">
        <p className='font-medium mr-4'>ダークモード</p>
        <ThemeToggle />
      </div>

    </nav>
  );
}