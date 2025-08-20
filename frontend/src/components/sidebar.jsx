import React from 'react';

const Sidebar = ({ categories, loadArticles }) => {
  return (
    <div className="w-1/4 bg-gray-200 p-4">
      <h2 className="text-lg font-bold">カテゴリ</h2>
      <ul>
        {categories.map((category) => (
          <li key={category} className="cursor-pointer hover:bg-gray-300" onClick={() => loadArticles(category)}>
            {category}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;
