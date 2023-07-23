import React, { useEffect, useState } from 'react'
import '../../App.css';
import Navbar from '../navbar';
import { useParams } from 'react-router-dom';

const InstalledApps = (pops) => {
  let {id1, id2} = useParams()
  const [sdks, setSdks] = useState([])
  const [sdk, setSdk] = useState()
  const [data,  setData] = useState([])

  useEffect(() => {
    // collect sdks
    const getSdksInfo = async() => {
      let res = await fetch("http://127.0.0.1:8000/api/sdks/",{
        'method': "GET",
        'headers': {
          'Content-Type': 'application/json',
        }
      });
      if (res.status===200){
        res = await res.json()
        // res = JSON.parse(res)
        res = res.map((item) => {
          return {"id":item.id, "name":item.name}
        })
        setSdks(res)
        console.log("res: ", res);
      }
    }
    if(sdks.length===0){
      getSdksInfo();
    }
    
    // getting data
    console.log(id1, id2);
    const getData = async (ids1, ids2) => {
      ids1 = ids1.split('_').map((item) => parseInt(item))
      ids2 = ids2.split('_').map((item) => parseInt(item))
      console.log("ids1: ", ids1)
      console.log("ids2: ", ids2)

      let res = await fetch("http://127.0.0.1:8000/api/sdk_apps_list/",{
        'method': "POST",
        'headers': {
          'Content-Type': 'application/json'
        },
        'body':JSON.stringify({
          "ids1":ids1,
          "ids2":ids2
        })
      })
      console.log(res.status)
      if (res.status===200){
        res = await res.json();
        console.log(res)
        console.log("res: ", res);
        setData(res)
      }else {
        console.log("error: ", res.status)
      }
    }

    getData(id1, id2)
  }, [])

  useEffect(()=>{
    console.log(data);
  }, [data])
  return (
    <div className='App'>
        <Navbar/>
        {/* page section */}
        <div className='container apps'>
          <div className='apps-head'>
            <h2>Current Installed Apps </h2>
          </div>
          <div>
            <table class="table table-striped table-bordered ">
              <thead>
                <tr>
                  <th scope="col">Id</th>
                  <th scope="col">Name</th>
                  <th scope="col">Company Url</th>
                  <th scope="col">Genre Id</th>
                  <th scope="col">Seller Name</th>
                  <th scope="col">Release Date</th>
                  <th scope="col">Artwork Large Url</th>
                  <th scope="col">5 Star Ratings</th>
                  <th scope="col">4 Star Ratings</th>
                  <th scope="col">3 Star Ratings</th>
                  <th scope="col">2 Star Ratings</th>
                  <th scope="col">1 Star Ratings</th>
                </tr>
              </thead>
              <tbody>
                {
                  data? (
                    data.map((item, indx) => {
                      return(
                        <tr key={indx+1}>
                          <th scope="row">{item.id}</th>
                          <td>{item.name}</td>
                          <td>{item.company_url}</td>
                          <td>{item.genre_id}</td>
                          <td>{item.seller_name}</td>
                          <td>{item.release_date}</td>
                          <td>{item.artwork_url}</td>
                          <td>{item.five_star_ratings}</td>
                          <td>{item.four_star_ratigns}</td>
                          <td>{item.three_star_ratings}</td>
                          <td>{item.two_star_ratings}</td>
                          <td>{item.one_star_ratings}</td>
                        </tr>
                      )
                    })
                  ):null
                }
              </tbody>
            </table>
          </div>
        </div>
    </div>
  )
}

export default InstalledApps