import { Component, OnInit, Input } from '@angular/core';
import { Location } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import {HttpErrorResponse } from '@angular/common/http'

import { Record } from '../record';
import { RecordService } from '../record.service';

@Component({
  selector: 'app-record-edit',
  templateUrl: './record-edit.component.html',
  styleUrls: ['./record-edit.component.css']
})
export class RecordEditComponent implements OnInit {
	
	@Input() record: Record;

	constructor(private route: ActivatedRoute, private recordService: RecordService, private location: Location) { }

	ngOnInit() {
		this.getRecord();
	}
	
	getRecord(): void {
		const id = + this.route.snapshot.paramMap.get('id');
		this.recordService.getRecord(id).subscribe(record => this.record = record);
	}
	
	save(): void {	
    // TODO Provide normal error handling.
		this.recordService.updateRecord(this.record).subscribe(
      success=> {
        this.goBack();
      }, (err:HttpErrorResponse)=>{console.log(err)}
      );
	}

	goBack(): void {
		this.location.back();
	}

}