import React, { useState, useEffect } from "react";

// export const useArticles = () => {
//     const [selectedCategory, selectCategory] = useState("");
//     const [mainCategories, setMainCategories] = useState([]);
//     const [articles, setArticles] = useState([]);

//     const dataDir = '../../data';
//     useEffect(() => {
//         window.api.readCategories(dataDir).then(setMainCategories).catch(console.error);
//     }, []);

//     return {
//         mainCategories,
//         selectedCategory, selectCategory
//     }
// }

export const useArticles = (docId) => {
  const [article, setArticle] = useState([]);

  useEffect(() => {
    if (!docId) return;

    fetch(`/documents/${docId}`)
      .then((res) => res.json())
      .then((data) => {
        setArticle(data);
      })
      .catch((err) => {
        console.error("記事の取得に失敗しました:", err);
      });
  }, [docId]);

  return { article };
}