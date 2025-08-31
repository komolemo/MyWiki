import { useState, useEffect } from "react";
import { getDocumentChunks } from "../services/documentService";

export const useArticles = (docId) => {
  const [article, setArticle] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!docId) return;

    getDocumentChunks(docId)
      .then(setArticle)
      .catch((err) => {
        console.error("記事の取得に失敗しました:", err);
        setError(err.message);
      });
  }, [docId]);

  return { article, error };
};