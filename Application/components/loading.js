
import '../styles/loading.css'

export default function Loading() {
    return (
        <div className="loading_screen">
            <div id="loader"></div>
            <div style={{ display: "none" }} id="myDiv" className="animate-bottom">
                <h2>Tada!</h2>
                <p>Some text in my newly loaded page..</p>
            </div>
        </div>
    )
}