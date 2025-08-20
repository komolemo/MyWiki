import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { PageMenu } from './pages/PageMenu';
import { PageArticle } from './pages/PageArticle';

const RouteConfig = () => {
  return (
    <Routes>
      <Route path="/" element={<PageMenu />} />
      <Route path="/article" element={<PageArticle />} />
    </Routes>
  );
};

export default RouteConfig;