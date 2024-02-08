* Load data
import delimited "data/raw/european_commission/ted-sample.csv", clear

* Only keep relevant variables
keep iso_country_code win_country_code award_value_euro

* Summarize award_value_euro
summarize award_value_euro, detail
// display `r(N)'
// display "Number of observations: `r(N)'"
// display "Mean: `r(mean)'"

*Drop outliers
 drop if award_value_euro > `r(p95)'
// drop if award_value_euro < `r(p5)'

*Plot the distribution of award_value_euro
hist award_value_euro

*Let's generate an indicator: 1(above mean), 0 otherwise
generate above_mean = 1
// replace above_mean = 0 if award_value_euro < `r(mean)'

*Let's generate an indicator: 1(above median), 0 otherwise
// generate above_median = (award_value_euro > `r(p50)')

*forvalues loop
forvalues i = 0/9 {
	display `i'
}

*foreach (1)
foreach vegetable in paprika aubergine carrot {
	di "`vegetable'"
}

* foreach(2)
foreach var of varlist iso_country_code win_country_code {
	count if strlen(`var') > 2
}

