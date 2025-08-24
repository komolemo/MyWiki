import React, { useState } from 'react';
import Sidebar from '../components/Sidebar';
import Article from '../components/Article';

export const PageArticle = () => {
    return (
        <>
            <div className="flex">
                <Sidebar/>
                <Article/>
            </div>
        </>
    )
}