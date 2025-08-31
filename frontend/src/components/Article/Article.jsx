import { useArticle } from "../../context/ArticleContext";
import ArticleChunk from "./ArticleChunk";

const Article = () => {
    const article = useArticle();

    return (
        <article className="flex-1 p-6 overflow-y-auto">
            <h1 className="text-2xl font-bold mb-4">ようこそ</h1>
            <p>これはローカルWikiのトップページです。</p>
            {article.map((chunk, index) => (
                <ArticleChunk key={index} chunk={chunk} />
            ))}
        </article>
    );
}

export default Article;