import FileUpload from "./components/FileUpload"

function App() {
  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <h1>Legal Text Classification</h1>
        <p>
          An academic machine learning system for categorizing legal documents.
        </p>

        <FileUpload />

        <div style={styles.footer}>
          <span>Department of Computer Science</span>
        </div>
      </div>
    </div>
  )
}

const styles = {
  page: {
    minHeight: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    padding: "20px"
  },
  card: {
    width: "440px",
    padding: "36px",
    borderRadius: "16px",

    /* Glass effect */
    background: "rgba(255, 255, 255, 0.85)",
    backdropFilter: "blur(10px)",

    boxShadow: "0 25px 50px rgba(0,0,0,0.25)"
  },
  footer: {
    marginTop: "28px",
    fontSize: "13px",
    color: "#64748b",
    textAlign: "center"
  }
}

export default App
