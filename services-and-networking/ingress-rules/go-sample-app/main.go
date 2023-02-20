package main

import (
    "github.com/gin-gonic/gin"
    "net/http"
    "os"
)

type user struct {
    UID string `json:"uid"`
    Username string `json:"username"`
    Email string `json:"email"`
    Age int `json:"age"`
}

func main(){
    router := gin.Default()

    // Loading HTMLs
    router.LoadHTMLFiles("index.html")

    // Serving index.html
    router.GET("/", func(c *gin.Context){
        c.HTML(http.StatusOK, "index.html", gin.H{})
    })

    // Serving api group
    router.GET("/api/v1/users", getAllUsers)
    api := router.Group("/api")

    {
        api.GET("/users", getAllUsers)
        // Could handle other methods / paths
        // api.POST("/user/:id", addUser)
    }

    var port string = os.Getenv("PORT")
    if (port == ""){
        port = "8080"
    }
    var host string = ":" + port
    if err := router.Run(host); err != nil{
        panic(err)
    }
}

func getAllUsers(c *gin.Context){
    var users = []user{
        {UID: "", Username: "carlos", Email: "carlosggflor@gmail.com", Age: 25},
        {UID: "", Username: "felps", Email: "felps@trimble.com", Age: 25},
    }

    c.IndentedJSON(http.StatusOK, users)
}
