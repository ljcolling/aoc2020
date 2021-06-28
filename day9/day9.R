require("tidyverse")

pre_length = 25

d = readr::read_csv("~/github/aoc2020/day9/puzzle_data.txt",  col_names = FALSE)
#d = readr::read_csv("~/github/aoc2020/day9/test_data.txt",  col_names = FALSE)

start_point = 1

checker <- function(d,pre_length,start_point){
    d %>% slice(start_point:(start_point + pre_length - 1)) %>% pull(X1) -> preamble
    length(preamble)
    cross_df(list(a = preamble, b = preamble)) %>% mutate(sum = a + b) %>% pull(sum) %>% unique(sums) -> sums

    checking <- d %>% pull(X1) %>% .[[start_point + pre_length]]

    return(tibble(value = checking, in_sum = checking %in% sums))
}

map_df(1:700, function(x) checker(d, pre_length,x)) %>% filter(in_sum == FALSE) %>% pull(value) -> code



x <- map_lgl(1: 1000, function(x) code %in% (d %>% slice(x:length(d$X1)) %>% pull(X1) %>% cumsum()))
s = min(which(x))

d %>% slice(s:length(d$X1)) %>% cumsum() -> cumsums
d %>% slice(s:length(d$X1)) -> d2
d2$cumsums <- cumsums$X1
d2$count = 1:length(d2$cumsums)
d2 %>% .[["X1"]] %>% .[1:17] %>% min()

d2 %>% .[["X1"]] %>% .[1:17] %>% min() -> min_value
d2 %>% .[["X1"]] %>% .[1:17] %>% max() -> max_value
min_value + max_value
