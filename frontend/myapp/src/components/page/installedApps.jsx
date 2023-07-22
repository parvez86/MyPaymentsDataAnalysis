import React, { useEffect, useState } from 'react'
import '../../App.css';
import Navbar from '../navbar';
import { useParams } from 'react-router-dom';

const InstalledApps = (pops) => {
  let {id} = useParams()
  const [sdk, setSdk] = useState()
  const [data,  setData] = useState({})

  useEffect(() => {
    console.log(id);
  }, [])

  return (
    <div className='App'>
        <Navbar/>
        {/* page section */}
        <div className='container apps'>
          <div className='apps-head'>
            <h2>Current Installed Apps using : </h2>
          </div>
          <div>
            <table class="table table-striped">
              <thead>
                <tr>
                  {/* <th scope="col">#</th> */}
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
                <tr>
                  <th scope="row">1</th>
                  <td>Mark</td>
                  <td>Otto</td>
                  <td>@mdo</td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>Jacob</td>
                  <td>Thornton</td>
                  <td>@fat</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td colspan="2">Larry the Bird</td>
                  <td>@twitter</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
    </div>
  )
}

export default InstalledApps