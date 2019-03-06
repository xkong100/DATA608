library(ggplot2)
library(dplyr)
library(shiny)

df <- read.csv('https://raw.githubusercontent.com/charleyferrari/CUNY_DATA_608/master/module3/data/cleaned-cdc-mortality-1999-2010-2.csv')


ui <- fluidPage(
  headerPanel('Rate'),
  sidebarPanel(
    selectInput('State', 'State', unique(df$State)),
  # selectInput('Year', 'Year', unique(df$Year)),
    selectInput('Cause', 'Cause of Death', unique(df$ICD.Chapter))
  ),
  mainPanel(
    plotOutput('plot1')
   
  )
)

server <- shinyServer(function(input, output) {
  
  selectedData <- reactive({
    dfSlice <- df %>%
      filter(State == input$State, ICD.Chapter == input$Cause)
    
    avg <- df %>%
      filter(ICD.Chapter==input$Cause) %>%
      group_by(Year) %>%
      summarise(rate=(sum(as.numeric(Deaths))/sum(as.numeric(Population))*10000))
  })

  
  output$plot1 <- renderPlot({
    
    dfSlice <- df %>%
      filter(State == input$State, ICD.Chapter == input$Cause)
    
    avg <- df %>%
      filter(ICD.Chapter==input$Cause) %>%
      group_by(Year) %>%
      summarise(rate=(sum(as.numeric(Deaths))/sum(as.numeric(Population))*10000))
      

    
    ggplot(selectedData(), aes(x=dfSlice$Year, y=dfSlice$Crude.Rate,color='red'))+ 
      geom_point(size=3) +
      geom_point(aes(x=avg$Year,y=avg$rate,color='black'),size=3)+
      scale_color_manual(
        name='Legend',
        values=c('red'='red','black'='black'),
        labels=c('National Average','State'))+
      
      theme_bw()+
      theme(panel.grid.major.y = element_blank(), axis.text = element_text(size =12),axis.title=element_text(size=18))+
     
      
      xlab("Year") +
      ylab("2010 Cause of Death  Mortality Rate") +
      ggtitle(input$cause)
    
  })
  

  
})

shinyApp(ui = ui, server = server)