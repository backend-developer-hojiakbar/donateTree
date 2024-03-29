function showhide() {
    // alert("okk")
    document.getElementById("compName").style.display = 'none'
    document.getElementById("flname").style.display = 'block'
    document.getElementById("fullName").style.display = 'none'
    document.getElementById("compWeb").style.display = 'none'
    document.getElementById("passCom").style.display = 'none'
    document.getElementById("passCit").style.display = 'block'
}

function showhideKom() {
    // alert("yess")
    document.getElementById("compName").style.display = 'block'
    document.getElementById("passCit").style.display = 'none'
    document.getElementById("flname").style.display = 'none'
    document.getElementById("fullName").style.display = 'block'
    document.getElementById("compWeb").style.display = 'block'
    document.getElementById("passCom").style.display = 'block'
    
}
