import { useState } from "react"

function FileUpload() {
  const [file, setFile] = useState(null)

  const handleFileChange = (e) => {
    setFile(e.target.files[0])
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
          opacity: file ? 1 : 0.6
        }}
        disabled={!file}
      >
        Classify Document
      </button>
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
