import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { Record } from '../record';
import { RecordService } from '../record.service';


@Component({
  selector: 'app-record-list',
  templateUrl: './record-list.component.html',
  styleUrls: ['./record-list.component.css']
})
export class RecordListComponent implements OnInit {

  records: Record[] = [];

  constructor(private route: ActivatedRoute, private recordService: RecordService, private location: Location) { }

	ngOnInit() {
		this.getRecords();
	}

	getRecords(): void {
		this.recordService.getRecords().subscribe(records => this.records = records);
	}
  
	delete(record: Record): void {
		this.recordService.deleteRecord(record).subscribe(success=> {this.getRecords();});		
	}

	goBack(): void {
		this.location.back();
	}

}
