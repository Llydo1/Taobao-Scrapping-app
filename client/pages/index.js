import { useEffect, useState } from "react";

export default function Home() {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        fetch("/hello/")
            .then((res) => res.json())
            .then((data) => {
                setData(data.message);
                console.log(data);
                setLoading(false);
            })
            .catch((e) => {
                console.log(e);
            });
    }, []);
    return (
        <div>
            <p> {!loading ? data : "Loading.."}</p>
        </div>
    );
}
