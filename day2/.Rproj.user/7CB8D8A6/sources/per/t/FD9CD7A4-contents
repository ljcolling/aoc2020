
require(tidyverse)
data <- readr::read_delim("data.txt", delim= " ", col_names = F) %>% magrittr::set_colnames(c("count","letter","password")) %>%
  mutate(letter = stringr::str_remove(letter,":")) %>%  separate(count, into = c("low","high"), sep = "-",remove = TRUE) 
  
  
data %>% pmap_dbl(function(low, high, letter, password) stringr::str_count(password, pattern = letter)) -> count
data %>% mutate(low = as.numeric(low), high = as.numeric(high)) -> data

data$count <- count
data  %>% filter(low >= count && high <= count)

data %>% select(low,high) %>% pmap(function(low,high) seq(low,high,1)) -> seqs

list(count = count,seqs = seqs) %>% pmap_dbl(function(count,seqs) count %in% seqs) -> acceptable

data$acceptable <- acceptable
data  %>% filter(count >= low &  count <= high)

### Day 2 - part 1

data %>% mutate(first = substr(password,low,low)) %>%
  mutate(second = substr(password,high,high)) %>%
  mutate(first = first == letter) %>%
  mutate(second = second == letter) %>%
  mutate(valid = xor(first,second)) %>%
  pull(valid) %>% sum()
