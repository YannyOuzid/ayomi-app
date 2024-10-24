import React, { useState } from "react";
import "./CalculatorBody.css"

const CalculatorBody = ({ bodyToHead, postEquation }) => {

    const [data, setData] = useState([])

    const addNewValue = (element) => {
        data.push(element)
        bodyToHead(data)
    }

    const cleanData = () => {
        data.splice(0, data.length)
        bodyToHead(data)
    }

    const removeLastData = () => {
        data.pop()
        bodyToHead(data)
    }

    const updateDataAfterPost = (body) => {
        postEquation(body);
        cleanData()
    }

    return (
        <div className="calculator-body">
            <div className="button-row">
                <button className="operator-button" onClick={() => cleanData()}>C</button>
                <button className="operator-button" onClick={() => removeLastData()}>&larr;</button>
                <button className="operator-button" onClick={() => addNewValue('/')}>/</button>
            </div>

            <div className="button-row">
                <button className="number-button" onClick={() => addNewValue(9)} >9</button>
                <button className="number-button" onClick={() => addNewValue(8)}>8</button>
                <button className="number-button" onClick={() => addNewValue(7)}>7</button>
                <button className="operator-button" onClick={() => addNewValue('*')}>*</button>
            </div>

            <div className="button-row">
                <button className="number-button" onClick={() => addNewValue(6)}>6</button>
                <button className="number-button" onClick={() => addNewValue(5)}>5</button>
                <button className="number-button" onClick={() => addNewValue(4)}>4</button>
                <button className="operator-button" onClick={() => addNewValue('-')}>-</button>
            </div>

            <div className="button-row">
                <button className="number-button" onClick={() => addNewValue(3)}>3</button>
                <button className="number-button" onClick={() => addNewValue(2)}>2</button>
                <button className="number-button" onClick={() => addNewValue(1)}>1</button>
                <button className="operator-button" onClick={() => addNewValue('+')}>+</button>
            </div>

            <div className="button-row">
                <button className="number-button" onClick={() => addNewValue(0)}>0</button>
                <button className="operator-button" onClick={() => updateDataAfterPost(data)}>=</button>
            </div>
        </div>
    )
}

export default CalculatorBody;