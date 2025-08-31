const ArticleChunk = ({ chunk }) => {
  const classNames = [
    chunk.color ? "bg-E97132" : "",
    chunk.bold ? "font-semibold" : ""
  ].filter(Boolean).join(" ");

  return (
    <span className={classNames}>
      {chunk.text}
      {chunk.br && <br />}
    </span>
  );
};

export default ArticleChunk;