const api = {
    fetchResults: async () => {
        const response = (await fetch("http://localhost:8000/api/calculator"));
        return response.json();
    },

    postEquation: async (body) => {
        const response = await fetch("http://localhost:8000/api/calculator", {
            headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json'
            },
            method: 'POST',
            mode: "cors",
            body: JSON.stringify({ equation: body, date: new Date().toISOString().split('T')[0] })
        })

        return response.json();
    },

    deleteFromHistory: async (id) => {
        const response = await fetch("http://localhost:8000/api/calculator/" + id, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            mode: "cors",
            method: 'DELETE'
        })

        return response.json();
    },

    fetchCsv: async () => {
        const response = (await fetch("http://localhost:8000/api/calculator/get_csv"));
        return response.json();
    }

}

export default api;