import React, { useState, useEffect } from "react";

export const useArticles = () => {
    const [selectedCategory, selectCategory] = useState("");
    const [mainCategories, setMainCategories] = useState([]);
    const [articles, setArticles] = useState([]);

    const dataDir = '../../data';
    useEffect(() => {
        window.api.readCategories(dataDir).then(setMainCategories).catch(console.error);
    }, []);

    return {
        mainCategories,
        selectedCategory, selectCategory
    }
}