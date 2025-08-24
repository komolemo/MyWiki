import React from 'react';

export default function Header({ toggleSidebar }) {
  return (
    <header className="flex items-center justify-between px-4 py-2 bg-white shadow">
        <div className="flex items-center gap-2 min-w-[200px]">
            <button onClick={toggleSidebar} className="text-2xl">☰</button>
            <div className="font-bold text-black text-lg">MY Career Wiki</div>
        </div>
        {/* <div className="flex flex-1 justify-center mx-4 max-w-lg">
            <input
                type="text"
                placeholder="検索"
                className="w-full border border-gray-300 rounded-l px-3 py-2 text-sm focus:outline-none"
            />
            <button className="border border-gray-300 border-l-0 rounded-r px-3 py-2 bg-gray-100 hover:bg-gray-200">
                🔍
            </button>
        </div> */}
        <div className="flex items-center w-full max-w-md border border-gray-300 rounded-full overflow-hidden bg-white">
            <input
                type="text"
                placeholder="検索..."
                className="flex-1 px-4 py-2 text-sm focus:outline-none"
            />
            <button className="px-4 py-2 bg-gray-100 hover:bg-gray-200 border-l border-gray-300 !rounded-none">
                🔍
            </button>
        </div>
        <button className="text-xl">⚙️</button>
    </header>
  );
}