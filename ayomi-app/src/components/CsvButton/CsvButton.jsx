import React from "react";
import './CsvButton.css'

const CsvButton = () => {

    return (
        <div className="button-container">
            <a className="csv-button" href="http://localhost:8000/api/results/get_csv">Download CSV</a>
        </div>

    )
}

export default CsvButton;