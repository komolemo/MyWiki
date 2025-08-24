import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import PageMenu from './pages/PageMenu';
// import { PageArticle } from './pages/PageArticle';

const RouteConfig = () => {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<PageMenu />} />
        {/* <Route path="/article" element={<PageArticle />} /> */}
      </Route>
    </Routes>
  );
};

export default RouteConfig;