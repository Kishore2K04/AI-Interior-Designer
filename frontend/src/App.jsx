import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);

  const uploadImage = async () => {
    if (!file) {
      alert("Select an image first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    alert(data.message);
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>AI Interior Designer</h1>

      <input
        type="file"
        accept="image/*"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={uploadImage}>
        Upload Image
      </button>
    </div>
  );
}

export default App;