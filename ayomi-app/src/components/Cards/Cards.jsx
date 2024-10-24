import React from "react";
import './Cards.css'

const Cards = ({ element, deleteData }) => {

    return (
        <div className="card">
            <div className="container">
                <h4><b>Date : {element.date}</b></h4>
                <h4><b>Equation : {element.equation}</b></h4>
                <p>Result : {element.result}</p>
            </div>
            <button className="delete-button" onClick={() => deleteData(element.id)}>Delete</button>
        </div>
    )
}

export default Cards;