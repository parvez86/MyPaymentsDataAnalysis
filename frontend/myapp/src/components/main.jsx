import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'

const Main = () => {
  const [sdks, setSdks] = useState([])
  const [sdkStats, setSdkStats] = useState()
  const [sdkNormStats, setSdkNormStats] = useState()
  const [sdknames, setSdkNames] = useState()
  const [sdkIds, setSdkIds] = useState("")

  let navigate = useNavigate()

  const getSdkAppStatsInfo = async(ids=undefined) => {
    let res;
    console.log(JSON.stringify({
      "sdk_ids":ids
    }))
    if(ids){
      res = await fetch("http://127.0.0.1:8000/api/current_sdk_apps_stat/",{
        'method': "POST",
        'headers': {
          'Content-Type': 'application/json'
        },
        'body':JSON.stringify({
          "sdk_ids":ids
        })
      });
    }else{
      res = await fetch("http://127.0.0.1:8000/api/current_sdk_apps_stat/",{
        'method': "GET",
        'headers': {
          'Content-Type': 'application/json'
        }
      }) ;
    }
    console.log(res.status)
    if (res.status===200){
      res = await res.json();
      console.log(res)
      res = JSON.parse(res);
      console.log("res: ", res);
      setSdkStats(res["original"])
      setSdkNormStats(res["norm"])
    }else {
      console.log("error: ", res.status)
    }
  }

  const onStatClick = (id) => {
    // e.preventDefault()
    // console.log("on stat",e.target.getAttribute('data-value'));
    console.log(id)
    
    let items = id.split('_')
    console.log(items)
    let ids1=[], ids2=[];
    if(items[0]==='none'){
        for (let sdk of sdknames){
            if(sdk !== 'none'){
              let index1 = sdks.findIndex((item) => item['name']===sdk)
              ids1=[...ids1, sdks[index1]['id']]
            }
        }
    }else{
      let index1 = sdks.findIndex((item) => item['name']===items[0])
      ids1 = [sdks[index1]['id']]
    }
    if(items[1]==='none'){
      for (let sdk of sdknames){
          console.log(sdk)
          if(sdk !== 'none'){
            let index2 = sdks.findIndex((item) => item['name']===sdk)
            ids2=[...ids2, sdks[index2]['id']]
          }
      }
    }else{
      let index2 = sdks.findIndex((item) => item['name']===items[1])
      ids2 = [sdks[index2]['id']]
    }
    ids1=ids1.join('_')
    ids2=ids2.join('_')
    console.log("ids1: ", ids1);
    console.log("ids2: ", ids2);
    navigate(`stats/${ids1}/${ids2}`)
  }
  
  useEffect(() => {
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
    if(!sdkStats){
      getSdkAppStatsInfo();
    }
  },[])

  useEffect(() => {
    console.log("sdk infos: ", sdks);
  }, [sdks])

  useEffect(() => {
    console.log("sdk stats infos: ", sdkStats);
    if (sdkStats){
      setSdkNames(Object.keys(sdkStats));
      Object.keys(sdkStats).map((x) => console.log(x, sdkStats[x]))
    }
  }, [sdkStats])

  useEffect(() => {
    console.log("sdk norm stats infos: ", sdkNormStats);
  }, [sdkNormStats])

  useEffect(() => {
    console.log(sdknames);
  }, [sdknames])

  const onSubmitButton= () => {
    console.log("input vals: ", sdkIds)
    let ids = sdkIds.replaceAll(" ","").split(',').map(item => parseInt(item, 10));
    console.log("ids: ", ids);
    getSdkAppStatsInfo(ids);
    setSdkIds("")
  }

  return (
    <div className='main-section'>
        <div className='payment-stat-section'>
            <div className='stat-header'>
                <h3>Payment SDK Statistics: </h3>
            </div>
            <div className='stat-input-box container'>
              <div>
                <h4>Custom Sdk Selection</h4>
              </div>
            <div className='sdk-ids mb-3'>
                <div className='left'>
                  <h6> Sdk ids: </h6>
                </div>
                <div className='right'>
                  {
                    sdks.length>0?(
                      <ul className='ids'>
                        {
                          sdks.map((item) => <li key={item.id}>{item.name}({item.id})</li>)
                        }
                      </ul>
                    ):null
                  }
                </div>
              </div>
              <div className='input-group mb-3 sdk-selection'>
                <div className='sdk-input'>
                  <span className="input-group-text">Select Sdk</span>
                  <input type="text" className="form-control" onChange={(e) => setSdkIds(e.target.value)} value={sdkIds} placeholder='sdk_id, sdk_id, ...'/>
                    {/* <label className='form-label select-label' htmlFor='select'>Select Sdk: </label> */}
                    {/* <datalist className="form select" id="sdklist" multiple>
                      <option value="1">One</option>
                      <option value="2">Two</option>
                      <option value="3">Three</option>
                      <option value="4">Four</option>
                      <option value="5">Five</option>
                    </datalist> */}
                  <button className="btn btn-outline-secondary" type="button" id="submit" onClick={() => onSubmitButton()}>submit</button>
                </div>                  
              </div>
            </div>
            <div className='sdk-stat'>
              <div className='sdk-stat-header'>
                <h4>Current Installed Apps of SDks:</h4>
              </div>
                
              <div className='sdk-stat-cmap container'>
                {/* <div className='cmap-header-row'>
                    <div className='header-empty'>
                      </div>
                      <div className='header-col'>
                          <p> PayPal</p>
                      </div>
                      <div className='header-col'>
                          <p> Stripe</p>
                      </div>
                      <div className='header-col'>
                          <p> Braintree</p>
                      </div>
                      <div className='header-col'>
                          <p> None</p>
                      </div>
                    </div> */}
                    {
                      sdkStats && sdknames? (
                        <div className='cmap-header-row'>
                          <div className='header-empty'>
                          </div>
                          {
                            sdknames.map(item =>
                              <div className='header-col'>
                                <p> {item}</p>
                            </div>
                            )
                          }
                        </div>
                      ):null
                    }
                    {
                       sdkStats && sdknames? (
                        Object.keys(sdkStats).map((item) => {
                          return (
                            <div className='row '>
                              <div className='col header-col-row' key={item}>
                                  <p>{item}</p>
                              </div>
                              {
                                Object.keys(sdkStats[item]).map(((sdk) => {
                                  return (
                                      sdkStats[item][sdk]===0?(
                                        <div className='col stat-col' key={`${item}-${sdk}`}>
                                          <p onClick={() => onStatClick(`${item}_${sdk}`)}>{sdkStats[item][sdk]}</p>
                                        </div>
                                      ):sdkStats[item][sdk]< 50?(
                                        <div className='col stat-col' key={`${item}-${sdk}`} style={{backgroundColor: `rgba(250, 250, 250, .5)`}}>
                                          <p onClick={() => onStatClick(`${item}_${sdk}`)}>{sdkStats[item][sdk]}</p>
                                        </div>
                                      ):sdkStats[item][sdk]< 500?(
                                        <div className='col stat-col' key={`${item}-${sdk}`} style={{backgroundColor: `rgba(225, 0, 0, 0.9)`}}>
                                          <p onClick={() => onStatClick(`${item}_${sdk}`)}>{sdkStats[item][sdk]}</p>
                                        </div>
                                      ):(
                                        <div className='col stat-col' key={`${item}-${sdk}`} style={{backgroundColor: `rgba(144, 11, 11, 0.9)`}}>
                                          <p onClick={() => onStatClick(`${item}_${sdk}`)}>{sdkStats[item][sdk]}</p>
                                        </div>
                                      )
                                  )
                                }))
                              }
                            </div>
                          )
                        })
                       ):null
                    }
                {/* <div className='row'>
                    <div className='col header-col-row'>
                        <p>PayPal</p>
                    </div>
                    <div className='col stat-col'>
                        <p>8</p>
                    </div>
                    <div className='col stat-col'>
                        <p>8</p>
                    </div>
                    <div className='col stat-col'>
                        <p>8</p>
                    </div>
                    <div className='col stat-col'>
                        <p>100</p>
                    </div>
                </div> */}
              </div>
            </div>
            <div className='sdk-stat'>
              <div className='sdk-stat-header'>
                <h4>Current Installed Apps of SDks(Norm):</h4>
              </div>
                
              <div className='sdk-stat-cmap container'>
                    {
                      sdkNormStats && sdknames? (
                        <div className='cmap-header-row'>
                          <div className='header-empty'>
                          </div>
                          {
                            sdknames.map(item =>
                              <div className='header-col'>
                                <p> {item}</p>
                            </div>
                            )
                          }
                        </div>
                      ):null
                    }
                    {
                       sdkNormStats && sdknames? (
                        Object.keys(sdkNormStats).map((item, indx) => {
                          return (
                            <div className='row '>
                              <div className='col header-col-row' key={item}>
                                  <p>{item}</p>
                              </div>
                              {
                                Object.keys(sdkNormStats[item]).map(((sdk) => {
                                  return (
                                    sdkNormStats[item][sdk] === 0.0?(
                                    <div className='col norm-col norm-stat-col' key={`${item}-${sdk}`}>
                                      <p onClick={() => onStatClick(`${item}_${sdk}`)}>{sdkNormStats[item][sdk]}%</p>
                                    </div>
                                    ):sdkNormStats[item][sdk]<0.3?(
                                    <div className='col norm-col norm-stat-col' key={`${item}-${sdk}`} style={{backgroundColor: `rgba(250, 250, 250, .5)`}}>
                                      <p onClick={() => onStatClick(`${item}_${sdk}`)}>{sdkNormStats[item][sdk]}%</p>
                                    </div>
                                    ):sdkNormStats[item][sdk]<0.5?(
                                    <div className='col norm-col norm-stat-col' key={`${item}-${sdk}`} style={{backgroundColor: `rgba(0, 0,255, 0.9)`}}>
                                      <p onClick={() => onStatClick(`${item}_${sdk}`)}>{sdkNormStats[item][sdk]}%</p>
                                    </div>
                                    ):sdkNormStats[item][sdk]<0.75?(
                                    <div className='col norm-col norm-stat-col' key={`${item}-${sdk}`} style={{backgroundColor: `rgba(12, 12, 191, 0.9)`}}>
                                      <p onClick={() => onStatClick(`${item}_${sdk}`)}>{sdkNormStats[item][sdk]}%</p>
                                    </div>
                                    ):(
                                    <div className='col norm-col norm-stat-col' key={`${item}-${sdk}`} style={{backgroundColor: `rgba(11, 11, 144, 0.9)`}}>
                                      <p onClick={() => onStatClick(`${item}_${sdk}`)}>{sdkNormStats[item][sdk]}%</p>
                                    </div>
                                    )
                                  )
                                }))
                              }
                            </div>
                          )
                        })
                       ):null
                    }
              </div>
            </div>
        </div>
    </div>
  )
}

export default Main