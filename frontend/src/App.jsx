import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);

  function handleFileChange(event) {
    setFile(event.target.files[0]);
  }

  async function handleSubmit(event) {
    event.preventDefault();

    if (!file) {
      alert("PDF를 선택해주세요.");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/documents", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();

    console.log(data);
  }
  return (
    <div>
      <h1>PDF RAG</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept="application/pdf"
          onChange={handleFileChange}
        />
        <button type="submit">업로드</button>
      </form>
    </div>
  );
}
export default App;
