import './App.css'
import {Input} from './components/ui/input'
import { Button } from './components/ui/button';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from './components/ui/card';
import { Alert,AlertTitle,AlertDescription } from './components/ui/alert';
import { useState , useEffect} from 'react';

function App() {
    let [domain, setDomain] = useState("")
    let [isLoading, setIsLoading] = useState(false)
    let [showAlert, setShowAlert] = useState(false)
    let [jobResults, setJobResults] = useState()
    let [domainInfo, setDomainInfo] = useState()
    let BackendUrl = import.meta.env.VITE_BACKEND_URL
    let [interval, setinterval] = useState()

    useEffect(() => {
        setTimeout(() =>{
            setShowAlert(false)
        } , 5000)
    }, [jobResults])

    useEffect(() => {
        if (domainInfo && Object.keys(domainInfo).length > 3) {
            clearInterval(interval)
            setIsLoading(false)
        }
    },[domainInfo])

    const getJobStatus = async () => {
        const response = await fetch(BackendUrl+"/get-domain-info?domain="+domain, {
          headers: {
              'accept': 'application/json',
          }
        })
        const data = await response.json()
        if(data.status ){
            delete data.status
            delete data.domain
            setDomainInfo(data)
        }
    }

    const startTldsearch = async () => {
        const response = await fetch(BackendUrl+"/sub-enum", {
            method: 'POST',
            headers: {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                domain : domain
            })
        })
        const data = await response.json()
        setJobResults(data.message)
        setShowAlert(true)
        let statusInterval = setInterval(getJobStatus, 5000)
        setinterval(statusInterval)
    }

    const handleDomainChange = (event) => {
        event.preventDefault()
        setIsLoading(false)
        setDomain(event.target.value)
    }

    const handleDomainSubmit = (event) => {
        event.preventDefault()
        setIsLoading(true)
        startTldsearch()
    }

    const handleDownload = (filename) => {
        fetch(BackendUrl+"/get-file/?filename="+filename, {
            method: 'GET',
            headers: {
                'accept': 'application/json',
            }
        }).then(response => {
            response.blob().then(blob => {
                const fileURL = window.URL.createObjectURL(blob);
                let alink = document.createElement('a');
                alink.href = fileURL;
                alink.download = filename;
                alink.click();
            })
        })
    }

 return (
     <div className="h-screen w-screen flex flex-col items-center justify-center">
        {showAlert && <Alert className="mt-4 absolute m-2 rounded border border-green-400 right-0 top-0 w-2/5">
                  <AlertTitle>Job Status</AlertTitle>
                      <AlertDescription>
                          {jobResults}
                      </AlertDescription>
        </Alert>}
        <div className="flex flex-row gap-4">
            <Input placeholder="Enter Top Level Domain" className="w-80 border rounded" onChange={handleDomainChange} value={domain}/>
            <Button variant="outline" className={"border rounded hover:bg-green-400 hover:text-white"+(isLoading ? " cursor-not-allowed" : "")} onClick={handleDomainSubmit}>{isLoading ? "Loading..." : "Go!"}</Button>
        </div>
     <div>
     {domainInfo && Object.entries(domainInfo).map(([key, value]) => (
         <Card className="mt-4 rounded hover:scale-125 transition duration-300 hover:bg-green-400 hover:text-white cursor-pointer" key={key} onClick={() => handleDownload(value)}>
             <CardHeader>
                 <CardTitle>{key.split("_")[0]}</CardTitle>
             </CardHeader>
             <CardContent>
                <div className="flex flex-row gap-4">
                 <p>{value}</p>
                 <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3" />
                </svg>
                </div>

             </CardContent>
         </Card>
     ))}
     </div>
     </div>
 )
}

export default App

