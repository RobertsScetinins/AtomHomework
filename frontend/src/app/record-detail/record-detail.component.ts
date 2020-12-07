import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { ActivatedRoute } from '@angular/router';

import { Record } from '../record';
import { RecordService } from '../record.service';

@Component({
  selector: 'app-record-detail',
  templateUrl: './record-detail.component.html',
  styleUrls: ['./record-detail.component.css']
})
export class RecordDetailComponent implements OnInit {

	record: Record;

	constructor(private route: ActivatedRoute, private recordService: RecordService, private location: Location) { }
	
	ngOnInit() {
		this.getRecord();
	}
	
	getRecord(): void {
		const id = + this.route.snapshot.paramMap.get('id');
		this.recordService.getRecord(id).subscribe(record => this.record = record);
	}

	goBack(): void {
		this.location.back();
	}

}
