import { useState } from "react"
import API from "../services/api"

function FileUpload() {
  const [file, setFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const handleFileChange = (e) => {
    setFile(e.target.files[0])
    setResult(null)
    setError(null)
  }

  const handleClassify = async () => {
    if (!file) return

    const formData = new FormData()
    formData.append("file", file)

    try {
      setLoading(true)

      const response = await API.post("/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })

      setResult(response.data)
    } catch (err) {
      console.error(err)
      setError("Failed to classify document. Is backend running?")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={styles.container}>
      <label style={styles.uploadRow}>
        <input
          type="file"
          accept=".pdf,.txt"
          onChange={handleFileChange}
          style={{ display: "none" }}
        />

        <div style={styles.left}>
          <span style={styles.icon}>📄</span>
          <div>
            <strong>Select Legal Document</strong>
            <div style={styles.subText}>PDF or TXT format</div>
          </div>
        </div>

        <div style={styles.buttonBox}>
          Browse
        </div>
      </label>

      {file && (
        <div style={styles.fileInfo}>
          ✔ Selected: {file.name}
        </div>
      )}

      <button
        style={{
          ...styles.classifyButton,
          opacity: file && !loading ? 1 : 0.6
        }}
        disabled={!file || loading}
        onClick={handleClassify}
      >
        {loading ? "Classifying..." : "Classify Document"}
      </button>

      {result && (
        <div style={{ marginTop: "16px", fontSize: "14px" }}>
          <strong>Prediction Result</strong>
          <pre style={{ marginTop: "8px" }}>
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}

      {error && (
        <div style={{ marginTop: "12px", color: "red", fontSize: "14px" }}>
          {error}
        </div>
      )}
    </div>
  )
}

const styles = {
  container: {
    marginTop: "24px"
  },
  uploadRow: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",

    border: "2px dashed #94a3b8",
    borderRadius: "10px",
    padding: "16px 18px",
    backgroundColor: "#f8fafc",
    cursor: "pointer"
  },
  left: {
    display: "flex",
    alignItems: "center",
    gap: "12px"
  },
  icon: {
    fontSize: "24px"
  },
  subText: {
    fontSize: "13px",
    color: "#64748b"
  },
  buttonBox: {
    padding: "6px 14px",
    borderRadius: "6px",
    backgroundColor: "#1e3a8a",
    color: "#ffffff",
    fontSize: "14px",
    fontWeight: "500"
  },
  fileInfo: {
    marginTop: "10px",
    fontSize: "14px",
    color: "#1e293b"
  },
  classifyButton: {
    width: "100%",
    marginTop: "18px",
    padding: "12px",
    borderRadius: "8px",
    border: "none",
    backgroundColor: "#1e3a8a",
    color: "#ffffff",
    fontSize: "16px",
    cursor: "pointer"
  }
}

export default FileUpload
