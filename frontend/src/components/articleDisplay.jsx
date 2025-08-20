import React from 'react';

const ArticleDisplay = ({ articles, loadArticle, content }) => {
  return (
    <div className="flex-1 p-4">
      <h2 className="text-lg font-bold">記事一覧</h2>
      <ul>
        {articles.map((article) => (
          <li key={article} className="cursor-pointer hover:bg-gray-300" onClick={() => loadArticle(article)}>
            {article}
          </li>
        ))}
      </ul>
      <div className="mt-4" dangerouslySetInnerHTML={{ __html: content }} />
    </div>
  );
};

export default ArticleDisplay;
