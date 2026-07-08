import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [objects, setObjects] = useState([]);
  const [layout, setLayout] = useState("");
  const [style, setStyle] = useState("Modern");
  const [generatedImage, setGeneratedImage] = useState("");

  const handleFileChange = (e) => {
    const selected = e.target.files[0];
    setFile(selected);

    if (selected) {
      setPreview(URL.createObjectURL(selected));
    } else {
      setPreview(null);
    }
  };

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

  const analyzeImage = async () => {
    if (!file) {
      alert("Select an image first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("style", style);

    const response = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      body: formData,
    });

  const data = await response.json();
    setObjects(data.objects);
    setLayout("http://127.0.0.1:8000" + data.layout);
  };


  const generateDesign = async () => {

  const response = await fetch("http://127.0.0.1:8000/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      style: style
    })
  });

  const data = await response.json();

  setGeneratedImage(data.image);
 };

  return (
    <div style={{ padding: "30px" }}>
      <h1>AI Interior Designer</h1>

      <input
        type="file"
        accept="image/*"
        onChange={handleFileChange}
      />

      <br />
      <br />

      {preview && (
        <img
          src={preview}
          alt="Preview"
          width="400"
        />
      )}

      <br />
      <br />

      <button onClick={uploadImage}>
        Upload Image
      </button>

      <button
        onClick={analyzeImage}
        style={{ marginLeft: "10px" }}
      >
        Analyze Room
        
      </button>

      <button onClick={generateDesign}>
      Generate Design
      </button>

      <h2>Detected Objects</h2>

    <ul>
      {objects.map((obj, index) => (
      <li key={index}>
      {obj.name}
      </li>
      ))}
    </ul>
    <h2>Select Interior Style</h2>

    <select
      value={style}
      onChange={(e) => setStyle(e.target.value)}
    >
      <option>Modern</option>
      <option>Minimal</option>
      <option>Luxury</option>
      <option>Scandinavian</option>
      <option>Industrial</option>
    </select>

  <p>
  Selected Style: <b>{style}</b>
  </p>

    <h2>Room Layout</h2>

  {layout && (
  <img
    src={layout}
    alt="Room Layout"
    width="400"
  />
  )}

    {generatedImage && (
  <>
    <h2>Generated Design</h2>

    <img
      src={generatedImage}
      alt="Generated Room"
      width="600"
    />
  </>
)}

      
    </div>
  );
}

export default App;