export const getDocumentChunks = async (docId) => {
  if (!docId) throw new Error("docId is required");

  // const res = await fetch(`/documents/${docId}`);
  const res = await fetch(`http://127.0.0.1:8000/documents/${docId}`);
  if (!res.ok) {
    throw new Error(`Failed to fetch document chunks: ${res.status}`);
  }

  return await res.json();
};