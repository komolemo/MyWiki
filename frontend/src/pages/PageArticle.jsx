import React, { useState } from 'react';
import Sidebar from '../components/sidebar';
import { Article } from '../components/article';

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