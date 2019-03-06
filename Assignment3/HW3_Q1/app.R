library(ggplot2)
library(dplyr)
library(shiny)

df <- read.csv("https://raw.githubusercontent.com/charleyferrari/CUNY_DATA_608/master/module3/data/cleaned-cdc-mortality-1999-2010-2.csv")

df_2010 <- subset(df, Year==2010)

ui <- fluidPage(
  headerPanel('Rank of each cause of Death across Different States'),
  sidebarPanel(
    selectInput('cause', 'Cause Of Death', unique(df_2010$ICD.Chapter))
  ),
  mainPanel(
    plotOutput('plot1'),
    verbatimTextOutput('stats')
  )
)



server <- shinyServer(function(input, output) {
  rates <- reactive({rates <- subset(df_2010,ICD.Chapter==input$cause)})
  output$plot1 <- renderPlot({
    ggplot(rates(), aes(x=reorder(State, Crude.Rate), y=Crude.Rate))+ coord_flip()+
    geom_point(shape=23, fill ="blue",color="red",size=3) +
      theme_bw()+
     theme(panel.grid.major.y = element_blank(), axis.text = element_text(size =7),axis.title=element_text(size=18))+

      xlab("State") +
      ylab("2010 Cause of Death  Mortality Rate") +
      ggtitle(input$cause)

    
  })
  
})
  


shinyApp(ui = ui, server = server)
