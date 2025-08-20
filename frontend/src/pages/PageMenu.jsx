import React, { useState, useEffect } from 'react';
import Sidebar from '../components/sidebar';
import ArticleDisplay from '../components/articleDisplay';

const dataDir = '../../data';

export const PageMenu = () => {
  const [categories, setCategories] = useState([]);
  const [articles, setArticles] = useState([]);
  const [selectedArticle, setSelectedArticle] = useState('');

  useEffect(() => {
    window.api.readCategories(dataDir).then(setCategories).catch(console.error);
  }, []);

  const loadArticles = (category) => {
    const categoryPath = `${dataDir}/${category}`;
    window.api.readArticles(categoryPath).then(setArticles).catch(console.error);
  };

  const loadArticle = (category, article) => {
    const articlePath = `${dataDir}/${category}/${article}`;
    window.api.readArticle(articlePath).then(setSelectedArticle).catch(console.error);
  };

  return (
    <div className="flex">
      <Sidebar categories={categories} loadArticles={loadArticles} />
      <ArticleDisplay articles={articles} loadArticle={loadArticle} content={selectedArticle} />
    </div>
  );
};

