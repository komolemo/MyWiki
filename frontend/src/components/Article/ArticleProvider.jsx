import { useState, useEffect } from "react";
import { ArticleContext } from "../../context/ArticleContext";
import { getDocumentChunks } from "../../services/documentService";

export const ArticleProvider = ({ docId, children }) => {
    const [article, setArticle] = useState([]);

    useEffect(() => {
        if (!docId) return;
        getDocumentChunks(docId).then(setArticle);
    }, [docId]);

    return (
        <ArticleContext.Provider value={article}>
            {children}
        </ArticleContext.Provider>
    );
};