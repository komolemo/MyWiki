import React, { useState } from 'react';
import Article from '../components/Article/Article';
import { ArticleProvider } from '../components/Article/ArticleProvider';
import { useParams } from "react-router-dom";

export const PageArticle = () => {
    const { docId } = useParams();
    return (
        <>
            <div className="flex">
                {/* <Sidebar/> */}
                <ArticleProvider docId={docId}>
                    <Article/>
                </ArticleProvider>
            </div>
        </>
    )
}