import React, { useState, useEffect } from "react";
import Calculator from "../../components/Calculator/Calculator";
import Cards from "../../components/Cards/Cards"
import "./Home.css"
import api from "../../services/api";
import CsvButton from "../../components/CsvButton/CsvButton";

const Home = () => {
    const [data, setData] = useState('');
    const [result, setResult] = useState("");

    useEffect(() => {
        getData();
    }, [])

    const getData = async () => {
        api.fetchResults().then((res) => setData(res));
    }

    const deleteData = async (id) => {
        api.deleteFromHistory(id).then(() => getData());
    }

    const postEquation = async (body) => {
        api.postEquation(body).then((res) => {
            setResult(res.result)
            getData()
        }).catch(err => { console.log(err); setResult("ERROR") });
    }

    return (
        <div className="home">
            <div className="calculator-side">
                <Calculator postEquation={postEquation} result={result}></Calculator>
            </div>
            <div className="card-side">
                <div className="card-list">
                    <CsvButton></CsvButton>
                    {data && data.map((element) => {
                        return (<Cards element={element} deleteData={deleteData}></Cards>)
                    })}
                </div>
            </div>
        </div>
    )
}

export default Home;