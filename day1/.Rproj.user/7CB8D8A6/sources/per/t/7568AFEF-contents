require(tidyverse)



# Day 1 part 2
data <- readr::read_csv("data.txt")

data %>% mutate(a = data, b = data) %>% 
  select(a,b) %>% purrr::cross_df() -> cross_data

cross_data %>% mutate(c = a + b) %>% filter(c < 2020) %>%
  mutate(diff = 2020 - c) %>% 
  filter(diff >= min(a)) %>% 
  filter(diff %in% a) %>%
  select(a,b,diff) %>% unlist() %>%
  as.numeric() %>% unique() %>%
  prod()
