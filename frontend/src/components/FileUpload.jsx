import { useState } from "react"
import API from "../services/api"

function FileUpload() {
  const [file, setFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [progress, setProgress] = useState(0)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const handleFileChange = (e) => {
    setFile(e.target.files[0])
    setResult(null)
    setError(null)
    setProgress(0)
  }

  const simulateDelay = (ms) =>
    new Promise((resolve) => setTimeout(resolve, ms))

  const handleClassify = async () => {
    if (!file) return

    const formData = new FormData()
    formData.append("file", file)

    try {
      setLoading(true)
      setProgress(0)

      // ⏳ Fake upload progress
      let fakeProgress = 0
      const interval = setInterval(() => {
        fakeProgress += 10
        if (fakeProgress <= 90) {
          setProgress(fakeProgress)
        }
      }, 300)

      // ⏳ Fake processing delay
      await simulateDelay(2000)

      const response = await API.post("/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })

      clearInterval(interval)
      setProgress(100)

      // ⏳ Final delay before showing result
      await simulateDelay(800)

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
        {loading ? "Analyzing Document..." : "Classify Document"}
      </button>

      {/* 🔵 Progress Bar */}
      {loading && (
        <div style={styles.progressContainer}>
          <div
            style={{
              ...styles.progressBar,
              width: `${progress}%`
            }}
          />
        </div>
      )}

      {/* 🧠 Clean Result UI */}
      {result && (
        <div style={styles.resultBox}>
          <h3 style={{ marginBottom: "8px" }}>Prediction Result</h3>

          <div>
            <strong>Article:</strong> {result.article || "Unknown"}
          </div>

          <div>
            <strong>Description:</strong> {result.description || "Unknown"}
          </div>

          {result.confidence !== null && result.confidence !== undefined && (
            <div>
              <strong>Confidence:</strong> {result.confidence}%
            </div>
          )}
        </div>
      )}

      {error && (
        <div style={styles.errorBox}>
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
  },

  /* Progress bar styles */
  progressContainer: {
    marginTop: "14px",
    height: "10px",
    width: "100%",
    backgroundColor: "#e5e7eb",
    borderRadius: "6px",
    overflow: "hidden"
  },
  progressBar: {
    height: "100%",
    backgroundColor: "#1e3a8a",
    transition: "width 0.3s ease"
  },
  resultBox: {
    marginTop: "18px",
    padding: "14px",
    borderRadius: "8px",
    backgroundColor: "#ecfeff",
    border: "1px solid #67e8f9",
    fontSize: "14px",
    color: "#0f172a"
  },
  errorBox: {
    marginTop: "14px",
    color: "#b91c1c",
    fontSize: "14px"
  }
}

export default FileUpload
