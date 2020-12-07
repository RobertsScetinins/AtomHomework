import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

import { Statistics } from '../statistics';
import { StatisticsService } from '../statistics.service';

@Component({
  selector: 'app-statistics',
  templateUrl: './statistics.component.html',
  styleUrls: ['./statistics.component.css']
})

export class StatisticsComponent implements OnInit {

	statistics: Statistics;

	constructor(private statisticsService: StatisticsService, private location: Location) { }
	
	ngOnInit() {
		this.getStatistics();
	}
	
  getStatistics(): void {
		this.statisticsService.getStatistics().subscribe(statistics => this.statistics = statistics);
  }

	goBack(): void {
		this.location.back();
	}

}


